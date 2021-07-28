import dash
import dash_core_components as dcc
import dash_html_components as html
import base64

app = dash.Dash()

# Images
pets_encoded_image = base64.b64encode(open('assets/pets.png', 'rb').read())
wait_time_encoded_image=base64.b64encode(open('assets/clock.png', 'rb').read())
treatment_cost_encoded_image=base64.b64encode(open('assets/money.png', 'rb').read())

app.layout = html.Div(style={
    'background': '#f1f1f1',
    'color': '#34302d',
    'font-family': 'Arial',
    'margin': '0',
    'height' : '600px'
},children=[
    html.H1(
        children='Petclinic Analytics',
        style={
            'textAlign': 'center',
            'background': '#34302d',
            'color': '#6db33f',
            'margin': '0'
        }
    ),
    #html.Img(src='data:image/png;base64,{}'.format(pets_encoded_image)),
    html.Div(children='Real-time recommendation engine for Petclinics', style={
        'textAlign': 'center',
        'fontFamily': 'cursive',
        'background': '#34302d',
        'color': '#6db33f' 
    }),
    html.Label(children='Treatment Cost',style={'margin-top': '10px', 'padding-left': '5px'}),
    html.Div(style={
            'margin-top' : '10px',
            'padding' : '10px',
            'width': '50%'
        }, children=[
        dcc.Slider(
            id='treatment-cost-slider',
            min=20,
            max=150,
            step=1,
            value=100,
            marks={20:"$20",150:"$150"}
        ),
        #html.Img(src='data:image/png;base64,{}'.format(treatment_cost_encoded_image)),
        html.Br(),
        html.Div(id='slider-output-container', style={
            'color': '#996600',
            'margin-bottom': '10px'
        })
    ]),
    html.Label(children='Wait Times',style={'padding-left': '5px'}),
    html.Div(style={
            'margin-top' : '10px',
            'padding' : '5px',
            'width': '50%'
        }, children=[
        dcc.Slider(
            id='wait-time-slider',
            min=0,
            max=60,
            step=5,
            value=15,
            marks={15:"15 minutes",180:"180 minutes"}
        ),
        #html.Img(src='data:image/png;base64,{}'.format(wait_time_encoded_image)),
        html.Br(),
        html.Div(id='slider-output-container-2', style={
            'color': '#996600'
        }),
        html.Br(),
        html.Div(id='recommendation-score')
    ])
])

predictors = { "treatment_cost": 0, "wait_time": 0 }
style_recommended  = { "color": "green",  "font-weight": "bold", "font-size": "larger" }
style_not_recommended = { "color": "red", "font-weight": "bold", "font-size": "larger"  }

@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('treatment-cost-slider', 'value')])
def update_treatment_cost(value):
    return '${}'.format(value)

@app.callback(
    dash.dependencies.Output('slider-output-container-2', 'children'),
    [dash.dependencies.Input('wait-time-slider', 'value')])
def update_treatment_cost(value):
    return '{} minutes'.format(value)

@app.callback(
    dash.dependencies.Output('recommendation-score', 'children'),
    [dash.dependencies.Input('wait-time-slider', 'value'),dash.dependencies.Input('treatment-cost-slider', 'value')])
def update_recommendation(wait_time,treatment_cost):
    predictors["wait_time"] = wait_time
    predictors["treatment_cost"] = treatment_cost
    score = predict_temp(predictors) 
    print(score)
    return [
        html.Span('{}'.format("Recommended" if score else "Not Recommended"), 
        style=style_recommended if score else style_not_recommended)
    ]

def predict_temp(input):
    return (input["treatment_cost"] < 100 or input["wait_time"] < 23)

def predict(input):
    model = get_model()
    score = input['interval'] = 0
    features = ['interval','treatment_cost','wait_time']
    for idx, weight in model.coef:
        score += weight * input[ features[idx] ]
    return int(1 / (1 + exp(-score)))

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
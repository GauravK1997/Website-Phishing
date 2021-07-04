from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('website_phishing_svc.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        
        SFH = int(request.form['SFH'])
        
        popUpWidnow = int(request.form['popUpWidnow'])
       
        SSLfinal_State = int(request.form['SSLfinal_State'])
       
        Request_URL = int(request.form['Request_URL'])
        
        URL_of_Anchor = int(request.form['URL_of_Anchor'])
        
        web_traffic = int(request.form['web_traffic'])
        
        URL_Length = int(request.form['URL_Length'])
        
        age_of_domain = int(request.form['age_of_domain'])
        
        having_IP_Address = int(request.form['having_IP_Address'])
                    
            
        prediction=model.predict([[SFH, popUpWidnow, SSLfinal_State, Request_URL, URL_of_Anchor, web_traffic, URL_Length, age_of_domain, having_IP_Address]])
        
        output = prediction

        if output == 0:
            return render_template('index.html',prediction_text="The website is Suspicious")
        elif output == 1:
            return render_template('index.html',prediction_text="The website is Legitimate")
        elif output == -1:
            return render_template('index.html',prediction_text="The website is Phishy")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CardioData, PredictPipeline

application = Flask(__name__)

app=application

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("predict.html")
    elif request.method == "POST":
        data = CardioData(
            age=int(request.form.get('age')) * 365,
            gender=request.form.get('gender'),
            height=float(request.form.get('height')),
            weight=float(request.form.get('weight')),
            ap_hi=float(request.form.get('ap_hi')),
            ap_lo=float(request.form.get('ap_lo')),
            cholesterol=request.form.get('cholesterol'),
            gluc=request.form.get('gluc'),
            smoke=int(request.form.get('smoke')),
            alco=int(request.form.get('alco')),
            active=int(request.form.get('active'))
        )
        pred_df = data.get_data_as_frame()
        print (pred_df)

        predict_pipeline = PredictPipeline()
        print("created predic pipeline")
        results = predict_pipeline.predict(pred_df)
        print("found results: ", results)

        return render_template("predict.html", results=results[0])
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
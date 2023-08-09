from flask import Flask, jsonify, request, render_template
from utils import FitnessTracker
import pickle

app= Flask(__name__)

@app.route('/')
def home():
    #return jsonify({"Result":"Successful"})
    return render_template("sample.html")

@app.route('/FitnessTracker', methods = ["POST"])
def get_predicted_insight():
    data = request.form
    print("Data :", data)

 
    TotalSteps              = data["TotalSteps"]
    TotalDistance           = data["TotalDistance"]
    TrackerDistance         = data["TrackerDistance"]
    LoggedActivitiesDistance= data["LoggedActivitiesDistance"]
    VeryActiveDistance      = data["VeryActiveDistance"]
    LightActiveDistance     = data["LightActiveDistance"]
    SedentaryActiveDistance = data["SedentaryActiveDistance"]
    VeryActiveMinutes       = data["VeryActiveMinutes"]
    FairlyActiveMinutes     = data["FairlyActiveMinutes"]
    LightlyActiveMinutes    = data["LightlyActiveMinutes"]
    SedentaryMinutes        = data["SedentaryMinutes"]
    DayOfTheWeek            = data["DayOfTheWeek"]
    TotalActiveMinutes      = data["TotalActiveMinutes"]
    TotalActiveHours        = data["TotalActiveHours"]
    
    

    obj1 = FitnessTracker()

    PREDICTED_INSIGHT1 = obj1.get_predicted_insight(TotalSteps,TotalDistance,TrackerDistance,LoggedActivitiesDistance,VeryActiveDistance,LightActiveDistance,SedentaryActiveDistance,VeryActiveMinutes,FairlyActiveMinutes,LightlyActiveMinutes,SedentaryMinutes,DayOfTheWeek,TotalActiveMinutes,TotalActiveHours)
    #return jsonify({"Return" : f"Calories burned is {PREDICTED_INSIGHT} kcals"})
    return render_template("sample.html", PREDICTED_INSIGHT = PREDICTED_INSIGHT1)

if __name__ == "__main__":
    app.run(host = "0.0.0.0" , port = 8080)
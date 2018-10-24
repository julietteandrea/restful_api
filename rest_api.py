from flask import Flask, jsonify, request
from api_model import connect_to_db, db, Car

app = Flask(__name__)
connect_to_db(app)

#an attempt to built a restful api from scratch.
@app.route("/getVehicleInfoService")
def get_info():
	#code below: grabs information from database instead of hardcoding.
	car = Car.query.filter_by(car_id="2").first()
	return jsonify({"service": "getVehicleInforService",
		"status": "200", "data":{"vin":{"type": "String",
		"value": car.vin},"color":{
		"type":"String",
		"value": car.color},
		"fourDoorSedan": {"type": "Boolean",
		"value":car.four_door},
		"twoDoorCoupe":{
		"type":"Boolean",
		"value":car.two_door},
		"driveTrain":{
		"type": "String",
		"value": car.drivetrain
		}
		}
		})

@app.route("/getSecurityStatusService")
def get_security():
	return jsonify({
	 "service": "getSecurityStatus",
		"status": "200",
		"data": {
			"doors": {
			"type": "Array",
			"values": [
				{
					"location": {
						"type": "String",
						"value": "frontLeft"
					},
					"locked": {
						"type": "Boolean",
						"value": "False"
					}},{
					"location": {
						"type": "String",
						"value": "frontRight"
					},
					"locked": {
						"type": "Boolean",
						"value": "True"
					}
				}
			]}}})

@app.route("/getEnergyService")
def get_energy():
	return jsonify({"service": "getEnergyService","status": "200",
			"data": {
				"tankLevel": {
					"type": "Number",
					"value": "30"
				},
				"batteryLevel": {
					"type": "Null",
					"value": "null"
				}}})

@app.route("/actionEngineService")
def engine_service():
	return jsonify ({
	"service": "actionEngine",
	"status": "200",
	"actionResult": {
		"status": "EXECUTED|FAILED"
	}
})




if __name__ == "__main__":
	app.run(debug=True)
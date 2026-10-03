from flask import Blueprint, request, jsonify
planners = Blueprint("planners", __name__)
@planners.route("/api/recommend", methods=["POST"])
def recommend():
    d=request.get_json(silent=True) or {}
    try:
        budget=float(d.get("budget",0)); kind=d.get("kind")
        if budget<=0: return jsonify(success=False,message="Enter a valid budget"),400
        if kind=="party":
            guests=int(d.get("guests",0))
            if guests<=0: return jsonify(success=False,message="Enter guest count"),400
            title=f'{d.get("event","Event")} plan for {guests} guests at {d.get("venue","venue")}'
            parts=[("Venue",.30),("Food and refreshments",.35),("Decoration",.15),("Cake",.10),("Miscellaneous",.10)]
        elif kind=="interior":
            title=f'Interior plan for {d.get("rooms","your rooms")}. Requested: {d.get("items","essentials")}'
            parts=[("Furniture",.40),("Fans and electricals",.20),("Lighting",.15),("Decor and essentials",.15),("Contingency",.10)]
        else: return jsonify(success=False,message="Choose a planner"),400
        plan=[{"item":n,"amount":round(budget*p,2)} for n,p in parts]
        return jsonify(success=True,title=title,plan=plan,total=round(sum(x["amount"] for x in plan),2))
    except (ValueError,TypeError): return jsonify(success=False,message="Check your entered values"),400

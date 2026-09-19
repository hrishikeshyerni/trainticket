from flask import Flask, render_template_string, request

app = Flask(__name__)

# Simple HTML template inside Python
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>🎬 Movie Booking</title>
    <style>
        body { font-family: Arial; background: #222; color: #fff; text-align: center; }
        .card { background: #333; padding: 20px; margin: 50px auto; width: 400px; border-radius: 10px; }
        input, select { width: 90%; padding: 10px; margin: 10px; border-radius: 5px; border: none; }
        button { padding: 10px 20px; background: #ffcc00; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background: #ff9900; }
    </style>
</head>
<body>
    <div class="card">
        <h2>🎬 Book Your Movie Ticket</h2>
        <form method="POST">
            <label>Movie:</label>
            <select name="movie" required>
                <option value="Inception">Inception</option>
                <option value="Interstellar">Interstellar</option>
                <option value="Avengers">Avengers</option>
            </select><br>
            
            <label>Date:</label>
            <input type="date" name="date" required><br>
            
            <label>Time:</label>
            <select name="time" required>
                <option value="10:00 AM">10:00 AM</option>
                <option value="2:00 PM">2:00 PM</option>
                <option value="6:00 PM">6:00 PM</option>
                <option value="9:00 PM">9:00 PM</option>
            </select><br>
            
            <button type="submit">Book Now</button>
        </form>
        {% if booking %}
        <div style="margin-top:20px; background:#444; padding:15px; border-radius:8px;">
            ✅ Booking Confirmed! <br>
            Movie: {{ booking['movie'] }} <br>
            Date: {{ booking['date'] }} <br>
            Time: {{ booking['time'] }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def booking():
    booking = None
    if request.method == "POST":
        booking = {
            "movie": request.form["movie"],
            "date": request.form["date"],
            "time": request.form["time"]
        }
    return render_template_string(html_template, booking=booking)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

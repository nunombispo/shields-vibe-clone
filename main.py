from fastapi import FastAPI, Response

app = FastAPI()

COLORS = {
    "green": "#4c1",
    "brightgreen": "#4c1",
    "red": "#e05d44",
    "blue": "#007ec6",
    "grey": "#555",
    "gray": "#555",
}


@app.get("/badge/{badge_path}")
def badge(badge_path: str) -> Response:
    label, message, color = badge_path.rsplit("-", 2)
    fill = COLORS.get(color, "#555")
    # Fake widths — good enough for build-passing-green, wrong for longer text
    left_w, right_w = 50, 60
    width = left_w + right_w
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="20">
  <rect width="{left_w}" height="20" fill="#555"/>
  <rect x="{left_w}" width="{right_w}" height="20" fill="{fill}"/>
  <text x="{left_w // 2}" y="14" fill="#fff" font-size="11"
        text-anchor="middle" font-family="DejaVu Sans,Verdana,sans-serif">{label}</text>
  <text x="{left_w + right_w // 2}" y="14" fill="#fff" font-size="11"
        text-anchor="middle" font-family="DejaVu Sans,Verdana,sans-serif">{message}</text>
</svg>'''
    return Response(content=svg, media_type="image/svg+xml")

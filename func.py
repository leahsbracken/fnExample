import io
import json

from fdk import response

director_dict = ({"Thor": "Kenneth Branagh","Iron Man": "John Favreau", "Spider-Man: Homecoming": "Jon Watts"})


def handler(ctx, data: io.BytesIO=None):
    movie = "Thor"
    try:
        body = json.loads(data.getvalue())
        movie = body.get("movie")
    except (Exception, ValueError) as ex:
        print(str(ex))

    director = director_dict[movie]
    pythonObject = {
    "movie": movie,
    "director": director
    }

    return response.Response(
        ctx, response_data=json.dumps(
            pythonObject),
        headers={"Content-Type": "application/json"}
    )

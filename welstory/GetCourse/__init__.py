import logging
from welstory import get_menu, RestaurantCode, MealType
import azure.functions as func

DEFAULT_CODE = RestaurantCode.MULTICAMPUS
DEFAULT_MEAL_TYPE = MealType.LUNCH


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("[GetCourse] processed a request.")

    code = req.params.get("code")
    if not code:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            code = req_body.get("code")

    meal_type = req.params.get("meal_type")
    if not meal_type:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            meal_type = req_body.get("meal_type")

    if not code:
        code = DEFAULT_CODE
    if not meal_type:
        meal_type = DEFAULT_MEAL_TYPE

    # if CODE:
    #     return func.HttpResponse(f"Hello {name}!")
    # else:
    #     return func.HttpResponse(
    #         "Please pass a name on the query string or in the request body",
    #         status_code=400,
    #     )

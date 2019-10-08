import logging
import json
from .welstory import get_menu, today, RestaurantCode, MealType
import azure.functions as func

DEFAULT_CODE = RestaurantCode.MULTICAMPUS
DEFAULT_MEAL_TYPE = MealType.LUNCH


def get_param(req, name, default):
    param = req.params.get(name)
    if not param:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            param = req_body.get(name)

    if not param:
        param = default

    return param


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("[GetCourse] processing a request.")

    code = get_param(req, "code", DEFAULT_CODE)
    meal_type = get_param(req, "meal_type", DEFAULT_MEAL_TYPE)
    date = get_param(req, "date", today())

    logging.info(f"[GetCourse] code={code}, meal_type={meal_type}, date={date}")
    return func.HttpResponse(
        json.dumps(
            get_menu(code=code, meal_type=meal_type, date=date), ensure_ascii=False
        ),
        status_code=200,
        headers={"Access-Control-Allow-Origin": "*"},
    )

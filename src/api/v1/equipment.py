import time
from typing import Optional

from fastapi import APIRouter, status
from pydantic import constr, BaseModel

router = APIRouter()

EquipmentID = constr(pattern = r'^[a-zA-Z0-9]{6,}$')

class EquipmentParametersModel(BaseModel):
    username: str
    password: str
    vlan: Optional[int]
    interfaces: list[int]

class PostEquipmentCpeRequest(BaseModel):
    timeoutInSeconds: int
    parameters: EquipmentParametersModel

class ResponseModel(BaseModel):
    code: int
    message: str

@router.post(
    path = '/equipment/cpe/{id}',
    responses = {
        status.HTTP_200_OK: {'model': ResponseModel, 'description': 'Successful Response'},
        status.HTTP_404_NOT_FOUND: {'model': ResponseModel, 'description': 'The requested equipment is not found'},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {'model': ResponseModel, 'description': 'Internal provisioning exception'},
    }
)
def post_equipment_cpe(id: EquipmentID, body: PostEquipmentCpeRequest):
    time.sleep(60)
    return ResponseModel(
        code = status.HTTP_200_OK,
        message = 'success',
    )
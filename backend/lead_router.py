from fastapi import APIRouter

router = APIRouter(prefix='/api/leads', tags=['leads'])

@router.get('/')
def get_leads():
    return {'items': []}

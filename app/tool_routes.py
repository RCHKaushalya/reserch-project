from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.database import engine
from app.tool_models import Tool, LendingRequest

router = APIRouter()

@router.post('/tools')
def list_tool(tool: Tool):
    with Session(engine) as session:
        session.add(tool)
        session.commit()
        session.refresh(tool)
        return tool

@router.get('/tools/{location}')
def get_available_tools(location: str):
    with Session(engine) as session:
        tools = session.exec(
            select(Tool).where(Tool.location == location, Tool.available == True)
        ).all()
        return tools

@router.post('/tools/request')
def request_tool(request: LendingRequest):
    with Session(engine) as session:
        tool = session.get(Tool, request.tool_id)
        if not tool or not tool.available:
            raise HTTPException(status_code=404, detail="Tool not available")
        
        session.add(request)
        session.commit()
        session.refresh(request)
        return {'message' : 'Request submitted', 'tool': tool.name}
    
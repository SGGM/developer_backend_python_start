from fastapi import APIRouter, HTTPException

from app.api import crud
from app.api.models import TrackPointSchema, TrackPointDB, TrackPayload, DeviceStats

router = APIRouter()


@router.post("/create_track_point", response_model=TrackPointDB, status_code=201)
async def create_track_point(payload: TrackPointSchema):
    track_point_id = await crud.post(payload)
    response_object = {
        "id": track_point_id,
        "device_id": payload.device_id,
        "x": payload.x,
        "y": payload.y,
        "z": payload.z,
    }

    return response_object

@router.post("/get_device_stats/{device_id}", response_model=DeviceStats)
async def get_device_stats(device_id: int):
    stats = await crud.get_device_stats(device_id=device_id)
    
    if stats["x_count"] == 0:
        raise HTTPException(status_code=404, detail="Not found")
    return stats

@router.post("/get_device_stats_in_range", response_model=DeviceStats)
async def get_device_stats_in_range(payload: TrackPayload):
    stats_in_range = await crud.get_device_stats_in_range(payload.device_id, payload.time_start, payload.time_end)

    if stats_in_range["x_count"] == 0:
        raise HTTPException(status_code=404, detail="Not found")
    return stats_in_range
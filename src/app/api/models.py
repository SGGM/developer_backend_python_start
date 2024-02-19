from datetime import datetime

from pydantic import BaseModel


class TrackPointSchema(BaseModel):
    device_id: int
    x: float
    y: float
    z: float

class TrackPointDB(TrackPointSchema):
    id: int

class TrackPayload(BaseModel):
    device_id: int
    time_start: datetime
    time_end: datetime

class DeviceStats(BaseModel):
    x_max: float | None
    x_min: float | None
    x_count: float | None
    x_sum: float | None
    x_median: float | None
    y_max: float | None
    y_min: float | None
    y_count: float | None
    y_sum: float | None
    y_median: float | None
    z_max: float | None
    z_min: float | None
    z_count: float | None
    z_sum: float | None
    z_median: float | None

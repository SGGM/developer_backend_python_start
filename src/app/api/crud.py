from datetime import datetime

from app.api.models import TrackPointSchema
from app.api.sql_queries import (
    make_query_max,
    make_query_min,
    make_query_sum,
    make_query_count,
    make_query_median,
    make_query_max_in_period,
    make_query_min_in_period,
    make_query_sum_in_period,
    make_query_count_in_period,
    make_query_median_in_period
)
from app.db import track_points, database


async def post(payload: TrackPointSchema):
    query = track_points.insert().values(device_id=payload.device_id, x=payload.x, y=payload.y, z=payload.z)
    return await database.execute(query=query)

async def get_device_stats(device_id: int):
    async with database:
        # x queries
        query_x_max = make_query_max("x")
        res_x_max = await database.execute(query=query_x_max, values={"device_id": device_id})

        query_x_min = make_query_min("x")
        res_x_min = await database.execute(query=query_x_min, values={"device_id": device_id})

        query_x_count = make_query_count("x")
        res_count = await database.execute(query=query_x_count, values={"device_id": device_id})

        query_x_sum = make_query_sum("x")
        res_x_sum = await database.execute(query=query_x_sum, values={"device_id": device_id})

        query_x_median = make_query_median("x")
        res_x_median = await database.execute(query=query_x_median, values={"device_id": device_id})


        # y queries
        query_y_max = make_query_max("y")
        res_y_max = await database.execute(query=query_y_max, values={"device_id": device_id})

        query_y_min = make_query_min("y")
        res_y_min = await database.execute(query=query_y_min, values={"device_id": device_id})

        query_y_sum = make_query_sum("y")
        res_y_sum = await database.execute(query=query_y_sum, values={"device_id": device_id})

        query_y_median = make_query_median("y")
        res_y_median = await database.execute(query=query_y_median, values={"device_id": device_id})


        # z queries
        query_z_max = make_query_max("z")
        res_z_max = await database.execute(query=query_z_max, values={"device_id": device_id})

        query_z_min = make_query_min("z")
        res_z_min = await database.execute(query=query_z_min, values={"device_id": device_id})

        query_z_sum = make_query_sum("z")
        res_z_sum = await database.execute(query=query_z_sum, values={"device_id": device_id})

        query_z_median = make_query_median("z")
        res_z_median = await database.execute(query=query_z_median, values={"device_id": device_id})

        return {
            "x_max": res_x_max,
            "x_min": res_x_min,
            "x_count": res_count,
            "x_sum": res_x_sum,
            "x_median": res_x_median,
            "y_max": res_y_max,
            "y_min": res_y_min,
            "y_count": res_count,
            "y_sum": res_y_sum,
            "y_median": res_y_median,
            "z_max": res_z_max,
            "z_min": res_z_min,
            "z_count": res_count,
            "z_sum": res_z_sum,
            "z_median": res_z_median,
        }
    

async def get_device_stats_in_range(device_id: int, time_start: datetime, time_end: datetime):
    async with database:
        # x queries
        query_x_max = make_query_max_in_period("x")
        res_x_max = await database.execute(
            query=query_x_max, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_x_min = make_query_min_in_period("x")
        res_x_min = await database.execute(
            query=query_x_min, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_count = make_query_count_in_period("x")
        res_count = await database.execute(
            query=query_count, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_x_sum = make_query_sum_in_period("x")
        res_x_sum = await database.execute(
            query=query_x_sum, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_x_median = make_query_median_in_period("x")
        res_x_median = await database.execute(
            query=query_x_median, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })


        # y queries
        query_y_max = make_query_max_in_period("y")
        res_y_max = await database.execute(
            query=query_y_max, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_y_min = make_query_min_in_period("y")
        res_y_min = await database.execute(
            query=query_y_min, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_y_sum = make_query_sum_in_period("y")
        res_y_sum = await database.execute(
            query=query_y_sum, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_y_median = make_query_median_in_period("y")
        res_y_median = await database.execute(
            query=query_y_median, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })


        # z queries
        query_z_max = make_query_max_in_period("z")
        res_z_max = await database.execute(
            query=query_z_max, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_z_min = make_query_min_in_period("z")
        res_z_min = await database.execute(
            query=query_z_min, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_z_sum = make_query_sum_in_period("z")
        res_z_sum = await database.execute(
            query=query_z_sum, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_z_median = make_query_median_in_period("z")
        res_z_median = await database.execute(
            query=query_z_median, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        return {
            "x_max": res_x_max,
            "x_min": res_x_min,
            "x_count": res_count,
            "x_sum": res_x_sum,
            "x_median": res_x_median,
            "y_max": res_y_max,
            "y_min": res_y_min,
            "y_count": res_count,
            "y_sum": res_y_sum,
            "y_median": res_y_median,
            "z_max": res_z_max,
            "z_min": res_z_min,
            "z_count": res_count,
            "z_sum": res_z_sum,
            "z_median": res_z_median,
        }

from datetime import datetime

from app.api.models import TrackPointSchema
from app.db import track_points, database


async def post(payload: TrackPointSchema):
    query = track_points.insert().values(device_id=payload.device_id, x=payload.x, y=payload.y, z=payload.z)
    return await database.execute(query=query)

async def get_device_stats(device_id: int):
    async with database:
        # x queries
        query_x_max = """
            SELECT MAX(x)
                FROM track_points
                WHERE track_points.device_id = :device_id
        """
        res_x_max = await database.execute(query=query_x_max, values={"device_id": device_id})

        query_x_min = """
            SELECT MIN(x)
                FROM track_points
                WHERE track_points.device_id = :device_id
        """
        res_x_min = await database.execute(query=query_x_min, values={"device_id": device_id})

        query_x_count = """
            SELECT COUNT(x)
                FROM track_points
                WHERE track_points.device_id = :device_id
        """
        res_count = await database.execute(query=query_x_count, values={"device_id": device_id})

        query_x_sum = """
            SELECT SUM(x)
                FROM track_points
                WHERE track_points.device_id = :device_id
        """
        res_x_sum = await database.execute(query=query_x_sum, values={"device_id": device_id})

        query_x_median = """
            SELECT
                PERCENTILE_CONT( 0.5 )
                    WITHIN GROUP (
                        ORDER BY x
                    ) AS median
            FROM track_points
            WHERE track_points.device_id = :device_id
        """
        res_x_median = await database.execute(query=query_x_median, values={"device_id": device_id})


        # y queries
        query_y_max = """
            SELECT MAX(y)
                FROM track_points
                WHERE track_points.device_id = :device_id
        """
        res_y_max = await database.execute(query=query_y_max, values={"device_id": device_id})

        query_y_min = """
            SELECT MIN(y)
                FROM track_points
                WHERE track_points.device_id = :device_id
        """
        res_y_min = await database.execute(query=query_y_min, values={"device_id": device_id})

        query_y_sum = """
            SELECT SUM(y)
                FROM track_points
                WHERE track_points.device_id = :device_id
        """
        res_y_sum = await database.execute(query=query_y_sum, values={"device_id": device_id})

        query_y_median = """
            SELECT
                PERCENTILE_CONT( 0.5 )
                    WITHIN GROUP (
                        ORDER BY y
                    ) AS median
            FROM track_points
            WHERE track_points.device_id = :device_id
        """
        res_y_median = await database.execute(query=query_y_median, values={"device_id": device_id})


        # z queries
        query_z_max = """
            SELECT MAX(z)
                FROM track_points
                WHERE track_points.device_id = :device_id
        """
        res_z_max = await database.execute(query=query_z_max, values={"device_id": device_id})

        query_z_min = """
            SELECT MIN(z)
                FROM track_points
                WHERE track_points.device_id = :device_id
        """
        res_z_min = await database.execute(query=query_z_min, values={"device_id": device_id})

        query_z_sum = """
            SELECT SUM(z)
                FROM track_points
                WHERE track_points.device_id = :device_id
        """
        res_z_sum = await database.execute(query=query_z_sum, values={"device_id": device_id})

        query_z_median = """
            SELECT
                PERCENTILE_CONT( 0.5 )
                    WITHIN GROUP (
                        ORDER BY z
                    ) AS median
            FROM track_points
            WHERE track_points.device_id = :device_id
        """
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
        query_x_max = """
            SELECT MAX(x)
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """
        res_x_max = await database.execute(
            query=query_x_max, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_x_min = """
            SELECT MIN(x)
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """
        res_x_min = await database.execute(
            query=query_x_min, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_count = """
            SELECT COUNT(x)
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """
        res_count = await database.execute(
            query=query_count, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_x_sum = """
            SELECT SUM(x)
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """
        res_x_sum = await database.execute(
            query=query_x_sum, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_x_median = """
            SELECT
                PERCENTILE_CONT( 0.5 )
                    WITHIN GROUP (
                        ORDER BY x
                    ) AS median
            FROM track_points
                WHERE track_points.device_id = :device_id
                    AND track_points.timestamp >= :time_start
                    AND track_points.timestamp <= :time_end
        """
        res_x_median = await database.execute(
            query=query_x_median, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })


        # y queries
        query_y_max = """
            SELECT MAX(y)
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """
        res_y_max = await database.execute(
            query=query_y_max, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_y_min = """
            SELECT MIN(y)
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """
        res_y_min = await database.execute(
            query=query_y_min, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_y_sum = """
            SELECT SUM(y)
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """
        res_y_sum = await database.execute(
            query=query_y_sum, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_y_median = """
            SELECT
                PERCENTILE_CONT( 0.5 )
                    WITHIN GROUP (
                        ORDER BY y
                    ) AS median
            FROM track_points
            WHERE track_points.device_id = :device_id
                AND track_points.timestamp >= :time_start
                AND track_points.timestamp <= :time_end
        """
        res_y_median = await database.execute(
            query=query_y_median, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })


        # z queries
        query_z_max = """
            SELECT MAX(z)
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """
        res_z_max = await database.execute(
            query=query_z_max, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_z_min = """
            SELECT MIN(z)
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """
        res_z_min = await database.execute(
            query=query_z_min, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_z_sum = """
            SELECT SUM(z)
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """
        res_z_sum = await database.execute(
            query=query_z_sum, values={
                "device_id": device_id,
                "time_start": time_start,
                "time_end": time_end
                })

        query_z_median = """
            SELECT
                PERCENTILE_CONT( 0.5 )
                    WITHIN GROUP (
                        ORDER BY z
                    ) AS median
            FROM track_points
            WHERE track_points.device_id = :device_id
                AND track_points.timestamp >= :time_start
                AND track_points.timestamp <= :time_end
        """
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

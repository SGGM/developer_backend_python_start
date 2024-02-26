# Without time period
def make_query_max(val: str) -> str:
    return f"""
        SELECT MAX({val})
            FROM track_points
            WHERE track_points.device_id = :device_id
    """

def make_query_min(val: str) -> str:
    return f"""
        SELECT MIN({val})
            FROM track_points
            WHERE track_points.device_id = :device_id
    """

def make_query_count(val: str) -> str:
    return f"""
        SELECT COUNT({val})
            FROM track_points
            WHERE track_points.device_id = :device_id
    """

def make_query_sum(val: str) -> str:
    return f"""
        SELECT SUM({val})
            FROM track_points
            WHERE track_points.device_id = :device_id
        """

def make_query_median(val: str) -> str:
    return f"""
        SELECT
            PERCENTILE_CONT( 0.5 )
                WITHIN GROUP (
                    ORDER BY {val}
                ) AS median
            FROM track_points
            WHERE track_points.device_id = :device_id
        """


# With time period
def make_query_max_in_period(val: str) -> str:
        return f"""
            SELECT MAX({val})
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """

def make_query_min_in_period(val: str) -> str:
        return f"""
            SELECT MIN({val})
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """

def make_query_sum_in_period(val: str) -> str:
        return f"""
            SELECT SUM({val})
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """

def make_query_count_in_period(val: str) -> str:
        return f"""
            SELECT COUNT({val})
                FROM track_points
                    WHERE track_points.device_id = :device_id
                        AND track_points.timestamp >= :time_start
                        AND track_points.timestamp <= :time_end
            
        """

def make_query_median_in_period(val: str) -> str:
        return f"""
            SELECT
                PERCENTILE_CONT( 0.5 )
                    WITHIN GROUP (
                        ORDER BY {val}
                    ) AS median
            FROM track_points
                WHERE track_points.device_id = :device_id
                    AND track_points.timestamp >= :time_start
                    AND track_points.timestamp <= :time_end
        """
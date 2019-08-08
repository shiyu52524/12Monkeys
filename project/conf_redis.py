import redis
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
l = len(redis.StrictRedis(connection_pool=pool).keys())
r1 = redis.StrictRedis(connection_pool=pool)
r2 = redis.Redis(host='localhost', port=6379, db=1)
r3 = redis.Redis(host='localhost', port=6379, db=10)
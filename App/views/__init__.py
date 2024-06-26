# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .routines import routine_views
from .workouts import workout_views


views = [user_views, index_views, auth_views, routine_views, workout_views] 
# blueprints must be added to this list
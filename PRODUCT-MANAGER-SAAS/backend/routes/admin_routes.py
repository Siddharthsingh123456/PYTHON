from flask import Blueprint

from utils.decorators import admin_required


admin_bp = Blueprint('admin', __name__)


@admin_bp.get('/stats')
@admin_required
def stats():
    return {"message": "Admin stats endpoint"}, 200

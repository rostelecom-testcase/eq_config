from src.api.routers_registry import RoutersRegistry

import src.api.v1.equipment as equipment

prefix = '/api/v1'
RoutersRegistry.add(equipment.router, prefix = prefix)
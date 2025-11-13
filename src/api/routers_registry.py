from fastapi import FastAPI, APIRouter


class RoutersRegistry:

    _routers = []

    @classmethod
    def add(cls, router: APIRouter, prefix: str = '', tags: list | None = None):
        if tags is None: tags = []
        cls._routers.append({
            'router': router,
            'prefix': prefix,
            'tags': tags,
        })

    @classmethod
    def init(cls, app: FastAPI):
        for router_info in cls._routers:
            print('registering router', router_info)
            app.include_router(
                router_info['router'],
                prefix = router_info['prefix'],
                tags = router_info['tags'],
            )
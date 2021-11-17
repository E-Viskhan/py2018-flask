import abc

from flask import request
from data.controller.database_controller import *


class BaseController(abc.ABC):
    TABLE = None
    COLUMNS = None

    @classmethod
    def get_all(cls):
        return build_get_all(cls.TABLE)()

    @classmethod
    def get_by_id(cls, id):
        return build_get_by_id(cls.TABLE)(id)

    @classmethod
    def create(cls):
        return build_create(cls.TABLE, cls.COLUMNS, [request.json[key] for key in cls.COLUMNS])()

    @classmethod
    def delete_by_id(cls, id):
        return build_delete(cls.TABLE)(id)

    @classmethod
    def replace_by_id(cls, id):
        """PUT"""
        return build_replace(cls.TABLE, cls.COLUMNS, [request.json[key] for key in cls.COLUMNS])(id)

    @classmethod
    def update_by_id(cls, id):
        """PATCH"""
        return build_update(cls.TABLE, cls.COLUMNS, request)(id)

    @classmethod
    def delete_all(cls, id):
        pass

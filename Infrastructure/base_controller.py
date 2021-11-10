import abc

from flask import request
from data.controller.database_controller import *


class BaseController(abc.ABC):

    @classmethod
    def get_all(cls, table):
        return build_get_all(table)()

    @classmethod
    def get_by_id(cls, table, id):
        return build_get_by_id(table)(id)

    @classmethod
    def create(cls, table, columns):
        return build_create(table, columns, [request.json[key] for key in columns])()

    @classmethod
    def delete_by_id(cls, table, id):
        return build_delete(table)(id)

    @classmethod
    def replace_by_id(cls, table, columns, id):
        """PUT"""
        return build_replace(table, columns, [request.json[key] for key in columns])(id)

    @classmethod
    def update_by_id(cls, table, columns, id):
        """PATCH"""
        return build_update(table, columns, request)(id)

    @classmethod
    def delete_all(cls, id):
        pass

"""This module is probably one of the most important,\
    allow me to dynamically import usecase with the good storage engine"""
import os
import re

from importlib import import_module


class Container:
    """This class defined a container

    Functions:
    ----------
    get_entity_name_from_usecase_name:
        get the entity_name from the usecase_name
    get_usecase:
        get the usecase from the usecase_name
    get_repository:
        get back the good DAO implementation
    get_usecase_repo:
        get back the good usecase and DAO implementation

    """

    @staticmethod
    def get_entity_name_from_usecase_name(usecase_name: str):
        """This function will get the entity_name for the usecase

        Parameters:
        -----------
        usecase_name: str
            The name of the usecase we want

        Returns:
        --------
        str
            The entity name

        """

        entity_name = ""
        uc_snake = re.sub(r'(?!^)([A-Z]+)', r'_\1', usecase_name).lower()

        for a, b, c in os.walk("gen_stix/src/gen_stix/entity"):
            if "__pycache__" not in a:
                for file in c:
                    entity_snakecase = re.split(r'\.py', file)[0]
                    if entity_snakecase in uc_snake:
                        entity_name = entity_snakecase
                        break
        return entity_name

    @staticmethod
    def get_usecase(usecase_name: str):
        """This function will get the usecase

        Parameters:
        -----------
        usecase_name: str
            The name of the usecase we want

        Returns:
        --------
        Class
            The usecase class

        """

        klass = None
        uc_snake = re.sub(r'(?!^)([A-Z]+)', r'_\1', usecase_name).lower()

        for a, b, c in os.walk("gen_stix"
                               "/src/gen_stix/usecase"):
            for file in c:
                if file == f"{uc_snake}.py":
                    module = import_module(f"{a.replace('/', '.')}.{uc_snake}")
                    klass = getattr(module, usecase_name)

        return klass

    @staticmethod
    def get_repository(entity_name: str, method: str):
        """This function will get the good DAO implementation

        Parameters:
        -----------
        entity_name: str
            The name of the entity we want
        method: str
            The name of the storage engine we want

        Returns:
        --------
        Class
            The right dao engine

        """

        klassrepo = None
        entity = ''.join(word.title() for word in entity_name.split('_'))

        for a, b, c in os.walk("gen_stix/src/app/repository"):
            for file in c:
                if file == f"{entity_name}_{method.lower()}_repository.py":
                    module = import_module(f"{a.replace('/', '.')}"
                                           f".{entity_name}_"
                                           f"{method.lower()}_repository")
                    klassrepo = getattr(module, f"{entity}{method}Repository")

        return klassrepo

    @staticmethod
    def get_usecase_repo(usecase_name: str, method: str):
        """This function will get the usecase with the good DAO implementation

        Parameters:
        -----------
        usecase_name: str
            The name of the usecase we want
        method: str
            The name of the storage engine we want

        Returns:
        --------
        Class
            The usecase with the right dao engine

        """

        klass = Container.get_usecase(usecase_name)
        entity_name = Container.get_entity_name_from_usecase_name(usecase_name)
        klassrepo = Container.get_repository(entity_name, method)

        return klass(klassrepo())

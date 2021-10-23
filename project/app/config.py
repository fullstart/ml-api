# -*- coding: utf-8 -*-
"""
Handling environment-specific configuration variables

@author: Andrey Aksenov
"""
import logging
import os
from functools import lru_cache

from pydantic import BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    """Storage for config settings."""
    
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)


@lru_cache()
def get_settings() -> BaseSettings:
    """
    Get current settings.

    Returns
    -------
    BaseSettings
        Return configuration settings.

    """
    log.info("Loading config settings from the environment")
    
    return Settings()

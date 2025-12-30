import ctypes
import logging

from ..proto.Neonize_pb2 import LogEntry

# Library loggers - NO configuration, let application configure
log = logging.getLogger(__name__)

clientlogger = logging.getLogger("whatsmeow.Client")
dblogger = logging.getLogger("Whatsmeow.Database")


def log_whatsmeow(binary: int, size: int):
    """Process whatsmeow log entry synchronously."""
    try:
        log_msg = LogEntry.FromString(ctypes.string_at(binary, size))
        if log_msg.Name == "Client":
            logger = clientlogger
        elif log_msg.Name == "Database":
            logger = dblogger
        else:
            name = log_msg.Name.replace("/", ".")
            logger = logging.getLogger(f"whatsmeow.{name}")
        level_fn = getattr(logger, log_msg.Level.lower(), logger.info)
        level_fn(log_msg.Message)
    except Exception:
        log.exception("Failed to handle WhatsMeow log")

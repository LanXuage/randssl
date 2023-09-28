#!/bin/env python3
import ssl
import random
import threading

# ECDH+AESGCM = [0xc02c, 0xc030, 0xc02b, 0xc02f]
# DH+AESGCM = [0x00a3, 0x009f, 0x00a2, 0x009e]
# ECDH+AES256 = [0xc0af, 0xc0ad, 0xc024, 0xc028, 0xc00a, 0xc014]


class SSLFactory(object):
    _instance = None
    lock = threading.Lock()

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            with cls.lock:
                if cls._instance is None:
                    cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        self.ciphers = [
            "ECDH+AESGCM",
            "DH+AESGCM",
            "ECDH+AES256",
            "DH+AES256",
            "ECDH+AES128",
            "DH+AES",
            "ECDH+HIGH",
            "DH+HIGH",
            "ECDH+3DES",
            "DH+3DES",
            "RSA+AESGCM",
            "RSA+AES",
            "RSA+HIGH",
            "RSA+3DES",
        ]
        self.suffix = ":!aNULL:!eNULL:!MD5"

    def generate_ssl_context(self, exclude=[]) -> ssl.SSLContext:
        ciphers = self.ciphers.copy()
        while True:
            random.shuffle(ciphers)
            if ciphers not in exclude:
                break
        context = ssl.create_default_context()
        context.set_ciphers(":".join(ciphers) + self.suffix)
        return context


def randssl(exclude=[]) -> ssl.SSLContext:
    return SSLFactory().generate_ssl_context(exclude=exclude)


COMMON_SSL_CONTEXTS = []


def rare_randssl() -> ssl.SSLContext:
    return randssl(exclude=COMMON_SSL_CONTEXTS)

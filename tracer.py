# Jaeger - Open Tracing.

from jaeger_client import Config

def init_jaeger_tracer(service_name=None):
    if service_name is None:
        raise "'service_name' Mandatory Field"
        
    config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
    config = Config(config=config, service_name=service_name, validate=True)
    return config.initialize_tracer()
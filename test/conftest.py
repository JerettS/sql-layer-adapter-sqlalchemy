from sqlalchemy.dialects import registry

registry.register("foundationdb", "sqlalchemy_foundationdb.dialect.psycopg2", "FDBPsycopg2Dialect")
registry.register("foundationdb.psycopg2", "sqlalchemy_foundationdb.dialect.psycopg2", "FDBPsycopg2Dialect")

from sqlalchemy.testing.plugin.pytestplugin import *

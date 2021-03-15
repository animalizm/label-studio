#!/bin/sh
# wait-for-it.sh

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

<<<<<<< HEAD
python3.8 label_studio/manage.py migrate 
=======
>>>>>>> 269f130a2cd9199f97f35aad9c614d1e48619b4f
>&2 echo "Postgres is up - executing command"
exec $cmd

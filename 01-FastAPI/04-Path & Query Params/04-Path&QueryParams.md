# Path & Query Params in FastAPI

## PATH PARAMETERS
dynamic segments in the URL path that can be used to capture values.

localhost:8000/items/42
In this example, 42 is a path parameter that represents the item_id.

## QUERY PARAMETERS
key-value pairs that are appended to the end of a URL after a question mark (?). They are used to filter, sort, or paginate data.

localhost:8000/items/?skip=0&limit=10
In this example, skip and limit are query parameters used for pagination.
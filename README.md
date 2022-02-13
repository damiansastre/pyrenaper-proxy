# pyrenaper-proxy

Proxy implementation for [pyrenaper](https://github.com/tagercito/pyrenaper)

## Documentation

[Postman Documentation](https://documenter.getpostman.com/view/4003274/UVeNm2nJ)
## Docker Instalation

Modify docker-compose with api keys

```
USERNAME: ''
PASSWORD: ''
```

The following command will build the docker image

```
docker-compose build
```

Finally run

```
docker-compose up
```

## Endpoints

### Full Integration
| URL        |  Description |
| ------------- |:----------:|
| /user/<user_id>  | User CRUD. 

## Extra endpoints

| URL        | Description |
| ------------- |:----------:|
| /decode      | Looks for ID barcodes and returns it's content| 


## Usage

* Create a user by passing a user_id by **POST** to the /user/ endpoint. 
* Validate Identity by passing an image of the front of the user ID by **PUT** to the user endpoint.
* (optional) Get user information by calling the /user/ endpoint via **GET**.
* (extra) To get the output of the barcode inside the image, the method /decode/ could be used.
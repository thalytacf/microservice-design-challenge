# API Design

This document describes the REST API design of the microservice, covering the available endpoints, input validations, payload examples, and performance requirements.

## Microservice Objective

To create a scalable and easy-to-maintain microservice that receives and stores large volumes of data, with strict input validation and efficient access to persisted information.

---

## Endpoints

### POST `/data`

Receives a JSON payload, validates the data, and stores it in the database.

* **Request Body:**

```json
{
  "id": 1,
  "name": "example",
  "value": 123.45
}
```

* **Validações:**

  * `id`: required, integer
  * `name`: required, string
  * `value`: required, decimal number

* **Responses:**

  * `201 Created`: item successfully created

  *`422 Unprocessable Entity`: invalid payload

---

### GET `/data`

Returns all stored data.

* **Response:**

```json
[
  {
    "id": 1,
    "name": "example",
    "value": 123.45
  },
  {
    "id": 2,
    "name": "another",
    "value": 678.90
  }
]
```

* **Status Code:**

 * `200 OK`: success

---

##Performance Considerations

* Endpoints must respond within 500ms under normal load.
* The architecture supports millions of records, with at most 10% degradation in response time.
* Database uses indexing to speed up read operations.

___

## Notes

* The API follows REST principles.
* All inputs are validated using Pydantic models.
* Horizontal scalability enables support for many simultaneous users.




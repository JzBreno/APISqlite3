Sure! Here is the README in English for your GitHub project:

---

# SQLite API

A simple API for interacting with a SQLite database, providing basic CRUD operations on the `clientes` table.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This API provides a straightforward interface for performing CRUD (Create, Read, Update, Delete) operations on a SQLite database. The operations are performed on the `clientes` table, which contains the fields `id`, `nome`, and `email`.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/sqlite-api.git
    cd sqlite-api
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Create the `clientes` table:
    ```python
    from main import Createtable, con

    Createtable(con)
    ```

2. Insert a record:
    ```python
    from main import InsertRegister, cur, con

    data = ('John Doe', 'john.doe@example.com')
    InsertRegister(cur, con, data)
    ```

3. Update a record:
    ```python
    from main import Updateregister, cur, con

    data = ('Jane Smith', 'jane.smith@example.com', 1)  # ID of the record to update
    Updateregister(cur, con, data)
    ```

4. Delete a record:
    ```python
    from main import Deleteregister, cur, con

    data = (1,)  # ID of the record to delete
    Deleteregister(cur, con, data)
    ```

5. Search for a client:
    ```python
    from main import Search_Client, cur

    client = Search_Client(cur, (2,))
    print(dict(client))
    ```

6. List all clients:
    ```python
    from main import List_Clients, cur

    clients = List_Clients(cur)
    for client in clients:
        print(dict(client))
    ```

## Examples

Below are examples of how to use the API in a Python script:

```python
from main import Createtable, InsertRegister, Updateregister, Deleteregister, Search_Client, List_Clients, con, cur

# Create the table
Createtable(con)

# Insert a record
InsertRegister(cur, con, ('Ana Clara', 'ana.clara@example.com'))

# Update a record
Updateregister(cur, con, ('Pedro Santos', 'pedro.santos@example.com', 1))

# Delete a record
Deleteregister(cur, con, (1,))

# Search for a client
client = Search_Client(cur, (2,))
print(dict(client))

# List all clients
clients = List_Clients(cur)
for client in clients:
    print(dict(client))
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the project
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is licensed under the [MIT License](LICENSE).

---

This README provides an overview of the project and detailed instructions on how to use it, making it ideal for publication on GitHub. Feel free to adjust it as necessary to better fit your specific project.

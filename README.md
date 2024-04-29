# Django_Assign
Requirements:
  1. Implement token-based authentication using Django REST Framework's
  built-in authentication classes. Only authenticated users should be able to
  perform CRUD operations.
  2. Users should be able to register an account, login, and retrieve their
  authentication token.
• Each artist object should have the following fields:
1) Artist Table
  ▪ Name
  ▪ User Instance (Foreign Key)
  ▪ Work (ManyToManyField)
2) Work Table
  ▪ Link
  ▪ Work Type
  • Youtube
  • Instagram
  • Other
❖ Important
  ▪ After each ‘Registration’ for a new user
  ▪ Make sure a new Artist object is created using signals
• Rest API
  ◦ Integrate API endpoints for the following operations:
  ▪ Retrieving a list of all works
  ▪ Create a new work
  ▪ Integrate Filtering with Work Type
  ▪ Integrate Search with Artist name

USER PERMISSIONS AND GROUP CONFIGURATION

Custom permissions defined in Book model:
- can_view
- can_create
- can_edit
- can_delete

User groups and associated permissions:
1. Viewers → can_view
2. Editors → can_view, can_create, can_edit
3. Admins → can_view, can_create, can_edit, can_delete

Views enforce permissions using @permission_required decorator:
- list_books → can_view
- create_book → can_create
- edit_book → can_edit
- delete_book → can_delete

To add a new user:
1. Create user in Django admin
2. Assign the user to one of the groups above

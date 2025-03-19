# Simple Vector Editor CLI

A simple vector editor with a command-line interface (CLI). It is designed to be easily extended, as the command processing is handled by separate objects of the `CommandHandler` class.

## Figure Types and Arguments

- **Point**: 2 coordinates  
- **Line**: 2 points (4 coordinates)  
- **Circle**: center point (2 coordinates) and radius  
- **Square**: diagonal (4 coordinates)
- **Oval**: center point(2 coordinates), radius_x, radius_y and angle 
- **Rectangle**: center point(2 coordinates), length, width and angle 

## Commands

### `exit`
- **Description**: Command that terminates the program.
- **Parameters**: No parameters
- **Example**: 
  ```
  exit

### `help`
- **Description**: Command that explains how commands work.
- **Parameters**: No parameters
- **Example**: 
  ```
  help
  ```

### `create`
- **Description**: Creates figures using the specified arguments.
- **Parameters**: `figure_type` and special figure parameters
- **Example**:
  ```
  create square 1 2 3 4
  ```

### `delete`
- **Description**: Deletes a figure by key.
- **Parameters**: `key`
- **Example**:
  ```
  delete 1
  ```

### `list`
- **Description**: Outputs a list of all figures with their indexes.
- **Parameters**: No parameters
- **Example**:
  ```
  list
  ```
  
### `save`
- **Description**: Saves a list of all figures to “figures_save.txt” or to a specified file.
- **Parameters**: `file_name`
- **Example**:
  ```
  save save_2.txt
  ```

### `load`
- **Description**: Loads all figures from the “figures_save.txt” file or from the specified file.
- **Parameters**: `file_name`
- **Example**:
  ```
  load save_2.txt
  ```
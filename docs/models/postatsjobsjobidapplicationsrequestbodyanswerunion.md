# PostAtsJobsJobIDApplicationsRequestBodyAnswerUnion

Answer to a question. This will be validated based on the question format and throw an error if the answer is invalid. Here is a description of each question type and the required answer format:

`TEXT` - Simply provide a "string" answer.

`SINGLE_SELECT` - Provide the ID of the answer as a string.

`MULTI_SELECT` - Provide a string array containing the question IDs of the selected options.

`BOOLEAN` - Either `true` or `false`.

`NUMBER` - A number.

`DATE` - Provide the answer as an ISO 8601 date string.

`FILE` - Please select Option 6 in the dropdown above to see the required format.


## Supported Types

### `str`

```python
value: str = /* values here */
```

### `bool`

```python
value: bool = /* values here */
```

### `float`

```python
value: float = /* values here */
```

### `List[str]`

```python
value: List[str] = /* values here */
```

### `datetime`

```python
value: datetime = /* values here */
```

### `models.PostAtsJobsJobIDApplicationsRequestBodyAnswer`

```python
value: models.PostAtsJobsJobIDApplicationsRequestBodyAnswer = /* values here */
```


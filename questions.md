### 1. Discuss your strategy and decisions implementing the application. Please,consider time complexity, effort cost, technologies used and any other variable that you understand important on your development process.

To implement the application I thought of a simple Django application, due to its practicality, performance, and its flexibility and scalability. It was simple to deal with models for each kind of data provided, import the CSV data and create views to show them accordingly as requested. And it would also take less time.

It didn't take that much effort, and since I wanted to deliver it on schedule I made a few trade-offs to make that possible. Here's some example:

- I wished to use Tailwind on the front-web. I thought it would be cool, but since I don't have that much experience with it, I thought bootstrap would get the job done.

- I'd love to add more tests to the project.

- I planned on working further on the models, treat some data better, maybe relate them, so we could use that to make some logics in Views better. There's room for improving logics in Views.

- I would have preferred to use a modern dependency manager like Poetry instead of a traditional requirements.txt, but given time constraints, I decided to prioritize functionality over tooling enhancements.

That said, I decided to add alternative ways of viewing the data — such as individual pages for each legislator. In addition to the bill vote summary, I also included a list of votes by legislator.

Overall, Django was solid and helpful, and its built-in management tools made development easier. Importing data was straightforward, and working with models felt smooth and efficient. Packaging the project with Docker also helps make it easier to run.


### 2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?

The current architecture supports model evolution. Adding new fields such as “Bill Voted On Date” would simply require extending the model and updating the views accordingly.

For a more complex case like “Co-Sponsors”, the model could be adjusted to support a many-to-many relationship, allowing multiple sponsors per bill. The views could then be updated to reflect this data structure and render it properly in the UI. Django’s ORM and templating system make this kind of change straightforward.

### 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

In this case, we could use Python’s built-in csv module to export data directly from the database. I would create a dedicated view or endpoint that processes the relevant data and returns a generated CSV file via HTTP response. This would allow users to download filtered or complete datasets based on specific criteria.

### 4. How long did you spend working on the assignment?

I’d estimate around 5 hours in total. I worked on it in smaller sessions rather than all at once, so this is a rough but fair approximation.
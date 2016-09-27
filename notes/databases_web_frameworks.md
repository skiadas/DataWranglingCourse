# Web Frameworks, and Flask

## Reading / References

- [Flask documentation](http://flask.pocoo.org/)

## Notes

### Web Frameworks

Any language that you choose for your web service or application will need certain features in common. This is what web frameworks can offer you, and all languages have usually more than one such framework.

- You need a way to process HTTP requests into a more meaningful form than just text, and similarly to prepare HTTP responses from your objects.
- You need to relate URL "routes" to specific functions in your application code.
- You need a way to use templates to automatically generate content.
- For web applications, you need some standard protections around submitting web forms.
- You need ways to maintain sessions of a user across multiple requests.
- You need easy connections to databases, integrated with the rest of the application.

Most web frameworks offer these and more. Some do it themselves, some allow for extensions. Some are very opinionated about exactly how you should structure your application, some give you more control over it. But whatever your project is, you would benefit from using some web framework, instead of reinventing the wheel.

### Flask

Flask is a Python Web Framework that in general takes a very minimalist approach. It offers some basic functionality, and leaves a lot of choices up to the programmer.

We will build a very simple messaging web service using Flask.

TODO

# RESTful APIs: The student evaluations case

## Reading / References

- [Restful Web Services](http://learning.acm.org/books/book_detail.cfm?id=1406352&type=safari), chapters 4 and 5. Optionally 6, 7, 8.
- [Current HTTP Specification](https://tools.ietf.org/html/draft-ietf-httpbis-p2-semantics-21) for some "light reading".

## Notes

We will now delve deeper into the API for our student evaluations.

Recall the entity-relation graph for the student evaluations database:

![](images/EvalsModel.png)

Here is a table of the various resources ([printable form](images/rest_printable.pdf))

-----------------------------------------------------------------------------------------------------------------------------
Resource      URI Scheme                     Properties  Links            GET               PUT        DELETE  POST
------------  -----------------------------  ----------- ---------------- ----------------- ---------- ------- --------------
students      /student                                   students         Student Links     N/A        N/A     Add student?

student       /student/{login}               login       enrollments      Student info.     Create?    Delete  Update info
                                             first                        enrollment links  Replace?           name
                                             last

enrollment    /enrollment/{section}/{login}  responded   student          Is enrolled?      Enroll     Remove  N/A
                                                         section                            student    student

roster        /enrollment/{section}                      enrollments      Class roster                 N/A     Mass enroll?
                                                         section

instructors   /instructor                                active instrs    Active instrs     N/A        N/A     Add instr?

instructor    /instructor/{login}            first last  sections         Instructor info   Create?    Remove? Update name
                                                         dept                               Replace?

admins        /admin                                     admins           Admin list        N/A        N/A     Add admin?

an admin      /admin/{login}                 first last                   ?????             Create?    Remove  Update info
                                                                                            Replace?

terms         /term                                      terms            terms list        N/A        N/A     Add term?

term          /term/{year}/{period}          dates       year             term info         New term?  Remove? Update dates
                                                         period           sections
                                                         sections         year, period

depts         /dept                                      depts            dept links        N/A        N/A     Add dept?
                                                         divisions?

a dept        /dept/{prefix}                 name        head             dept info         Create?    Remove? Update what?
                                                         members
                                                         parent
                                                         tags

courses       /course                                    courses          course list       N/A        N/A     Add course?
                                                                          depts?

a course      /course/{prefix}/{id}          descr       dept             course info       Create?    Remove? Update info
                                             no          sections         dept sections
                                                         tags             tags
                                                         parent

sections      /section                                   sections         section list      N/A        N/A     Add section?

a section     /section/{year}/{term}/{no}    state       course           section info      Create?    Remove? Update info?
                                                         roster
                                                         year
                                                         term

tags          /tag                                       tags             links to tags     N/A        N/A     Create new tag?

a tag         /tag/{tag}                     descr?      questions        tag info          Create?    Delete? Change descr?
                                                         depts?           questions?                           Change questions?
                                                         courses?
                                                         sections?

questions     /tag/{tag}/question                        questions        ordered           N/A        N/A     Add question.
                                                                          questions                            order?

question      /tag/{tag}/question/{id}       type        choices          question info     N/A        Remove? Update question.
                                             prompt                                                            order? choices?

answers?

evals?


-----------------------------------------------------------------------------------------------------------------------------

### Questions

- How should a section be assigned to an instructor?
- What should show up when we get an admin's page? Should it include links to the various resources *they* have access to?
- Should we characterize terms via year/period? What if we want ad-hoc terms?
- Do we need list of years as a resource?
- Do we need an individual year as a resource?
  - Should it be its own thing?
  - Or should terms allow a query to set the year, or just allow `/term/{year}`?
- How should we add a section to a term?
  - Option 1: Only do it by updating a section's information
  - Option 2: Set up the "term's course list" as a resource.
- Should we have a way to specifically add a new section of a course?
- Can we add query filtering in some of those lists?
- When to use query vs more slashes?
- Should questions be subordinate to a tag or on their own?
  - Need to somewhere coordinate tag question order.
  - Should a question be allowed to belong to multiple tags?

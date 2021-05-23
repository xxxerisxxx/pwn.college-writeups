## Instance 1
/bin/cat

``` $ cat /flag ```

## Instance 2
/bin/cp

* I don't have cat permissions on the flag for this challenge

Objective: Find a way to copy the file w/o copying over the file permisisons. 
Use ``` --no-preserve=mode ``` from man pages. 

![bincp](https://user-images.githubusercontent.com/45490952/119247762-4b911600-bb41-11eb-89ae-5694703887c1.PNG)

## Instance 3
/bin/more

```
$ more /flag
```
## Instance 4
/usr/bin/find

Read man pages and there is a way to execute commands using find.

``` -exec COMMAND {} ;```

Use \ to escape the characters.

![usrbinfind](https://user-images.githubusercontent.com/45490952/119248014-04a42000-bb43-11eb-853a-795a481c19cb.PNG)

## Instance 5
/usr/bin/head

``` $ head /flag ```

## Instance 6
/usr/bin/tail

``` $ tail /flag ```

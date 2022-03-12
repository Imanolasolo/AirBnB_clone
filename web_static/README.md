# 0x01. AirBnB clone - Web static
<div style="text-align: justify">

Thank you for visiting this repository which contain the `second step` towards building first `full web application`: the `AirBnB clone`. 
<div style="text-align: justify">
	
![hbnb](https://github.com/Alexoat76/AirBnB_clone/blob/main/assets/hbnb-logo.png?raw=true)
	
The project currently only implements the front-end `static web`. The goal of the project is to deploy on your server a simple copy of the `AirBnB website`.
![image](https://user-images.githubusercontent.com/86312558/158035254-680f52e7-bbfb-4c21-967e-514f1008febc.png)

# Getting Started :running:	
<div style="text-align: justify">
	
## Table of Contents
* [About](#about)
* [Requirements](#requirements)

* [Tasks](#tasks)
	* [Workbook](https://github.com/Alexoat76/AirBnB_clone/tree/main/assets/obsidian)
	* [Pseudocodes](https://github.com/Alexoat76/AirBnB_clone/tree/main/assets/pseudocodes)
* [Credits](#credits)

	
## About
	
Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

- Create simple HTML static pages

- Style guide

- Fake contents

- No Javascript

- No data loaded from anything
	
## Resources :books:

**Read or watch** :

[Learn to Code HTML & CSS (until “Creating Lists” included)](https://intranet.hbtn.io/rltoken/qq7qrSgdVRuD1kPd_jf7Fw)

[Inline Styles in HTML](https://intranet.hbtn.io/rltoken/xW69RnLZMt3AusI1SDvr8g)

[Specifics on CSS Specificity](https://intranet.hbtn.io/rltoken/sO3wz-QbhwYdKJqvokC4PA)

[CSS SpeciFishity](https://intranet.hbtn.io/rltoken/NvqQf3dgY64bb-QWC5Cueg)

[Introduction to HTML](https://intranet.hbtn.io/rltoken/STaxnOI5qv1enUuwIALelw)

[CSS](https://intranet.hbtn.io/rltoken/g-uj9Azx1rALX49xCZHK0w)

[MDN](https://intranet.hbtn.io/rltoken/El1BHRNNO2hPEcOt_XwF-Q)

[center boxes](https://intranet.hbtn.io/rltoken/HI0qRNDq20cgICIhO18kUQ)


#### **NOTE:** :notebook:

Our **`Workbook`** is created as `.md` type notes, we have used the **`OBSIDIAN`** application to be able to view and edit our notes.
In case the reader of this repository wants to view our workbook, please download the **`OBSIDIAN`** application from this [link](https://obsidian.md/download).

	

	
## Installation :computer:
	
- Clone this repository: `git clone "https://github.com/Imanolasolo/AirBnB_clone.git"`	
- Access AirBnb directory: `cd AirBnB_clone.`


## Tasks

**0. Inline styling**

Write an HTML page that displays a header and a footer.

Layout:

- Body:
    - no margin

    - no padding

- Header:

    - color #FF0000 (red)

    - height: 70px

    - width: 100%

- Footer:

    - color #00FF00 (green)

    - height: 60px

    - width: 100%

    - text Best School center vertically and horizontally

    - always at the bottom at the page

**Dependences**: [0-index.html](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/0-index.html)    

**1. Head styling**

Write an HTML page that displays a header and a footer by using the style tag in the head tag (same as 0-index.html)

Requirements:

    - You must use the header and footer tags

    - You are not allowed to import any files

    - No inline styling

    - You must use the style tag in the head tag

    - The layout must be exactly the same as `0-index.html`

**Dependences**: [1-index.html](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/1-index.html)

**2. CSS files**

Write an HTML page that displays a header and a footer by using CSS files (same as 1-index.html)

Requirements:

    - You must use the header and footer tags

    - No inline styling

    - You must have 3 CSS files
	 
    - The layout must be exactly the same as `1-index.html`
	
**Dependences**:

- [2-common.css](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/styles/2-common.css) : for global style (i.e. the body style)

- [styles/2-header.css](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/styles/2-header.css): for header style

- [styles/2-footer.css](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/styles/2-footer.css): for footer style

**3. Zoning done!**

Write an HTML page that displays a header and footer by using CSS files (same as 2-index.html)

Layout:

    Common:

        - no margin
        - no padding
        - font color: #484848
        - font size: 14px
        - font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;
        - icon in the browser tab
    Header:
        - color: white
        - height: 70px
        - width: 100%
        - border bottom 1px #CCCCCC
        - logo align on left and center vertically (20px space at the left)
    Footer:
        - color white
        - height: 60px
        - width: 100%
        - border top 1px #CCCCCC
        - text Best School center vertically and horizontally
        - always at the bottom at the page
Requirements:

    - No inline style
    - You are not allowed to use the img tag
    - You are not allowed to use the style tag in the head tag
    - All images must be stored in the images folder
    - You must have 3 CSS files

**Dependences:**  

[3-index.html](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/3-index.html) Main file 

[styles/3-common.css:](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/styles/3-common.css) for the global style (i.e body style)

[styles/3-header.css:](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/styles/3-header.css) for the header style

[styles/3-footer.css:](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/styles/3-footer.css) for the footer style

**4. Search!**

Write an HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on `3-index.html`)

    - Container:

        - between header and footer tags, add a div:

        - classname: container

        - max width 1000px

        - margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot)

        - center horizontally

    - Filter section:

        - tag section

        - classname filters

        - inside the .container

        - color white

        - height: 70px

        - width: 100% of the container

        - border 1px #DDDDDD with radius 4px

    Button search:

        - tag button

        - text Search

        - font size: 18px

        - inside the section filters

        - background color #FF5A5F

        - text color #FFFFFF

        - height: 48px

        - width: 20% of the section filters

        - no borders

        - border radius: 4px

        - center vertically and at 30px of the right border

        - change opacity to 90% when the mouse is on the button

Requirements:

    - You must use: header, footer, section, button tags

    - No inline style

    - You are not allowed to use the img tag

    - You are not allowed to use the style tag in the head tag

    - All images must be stored in the images folder

    - You must have 4 CSS files

**Dependences:** 

[4-index.html](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/4-index.html) Main file

[styles/4-common.css:](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/styles/4-common.css) for the global style (body and .container styles)

[styles/4-filters.css:](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/styles/4-filters.css) for the filters style

4-index.html won’t be W3C valid, don’t worry, it’s temporary

**5. More filters**

Write an HTML page that displays a header, footer and a filters box.

- Layout: (based on 4-index.html)

    - Locations and Amenities filters:
        - tag: div

        - classname: locations for location tag and amenities for the other

        - inside the section filters (same level as the button Search)

        - height: 100% of the section filters

        - width: 25% of the section filters

        - border right #DDDDDD 1px only for the first left filter

        - contains a title:

        - tag: h3

        - font weight: 600

        - text States or Amenities

        - contains a subtitle:

        - tag: h4

        - font weight: 400

        - font size: 14px

        - text with fake contents

**Dependences:** 

[5-index.html](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/5-index.html) Main file

[styles/5-filters.css:](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/styles/5-filters.css) for the filters style

6. It's (h)over

Write an HTML page that displays a header, footer and a filters box with dropdown.

- Layout: (based on 5-index.html)

    - Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter - div:

        - tag ul

        - classname popover

        - text should be fake now

        - inside each div

        - not displayed by default

        - color #FAFAFA

        - width same as the div filter

        - border #DDDDDD 1px with border radius 4px

        - no list display

        - Location filter has 2 levels of ul/li:

            - state -> cities

            - state name must be display in a h2 tag (font size 16px)

**Dependences:** 

[6-index.html](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/6-index.html) Main file

[styles/6-filters.css:](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/styles/6-filters.css) for the filters style

**7. Display results**

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

- Layout: (based on 6-index.html)

    - Add Places section:
        - tag: section
        - classname: places
        - same level as the filters section, inside .container
        - contains a title:
            - tag: h1
            - text: Places
            - align in the top left
            - font size: 30px
        - contains multiple “Places” as listing (horizontal or vertical) describe by:
            - tag: article
            - width: 390px
            - padding and margin 20px
            - border #FF5A5F 1px with radius 4px
            - contains the place name:
                - tag: h2
                - font size: 30px
                - center horizontally

	
**Dependences:** 

[6-index.html](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/6-index.html) Main file

[styles/6-filters.css:](https://github.com/Imanolasolo/AirBnB_clone/blob/main/web_static/styles/6-filters.css) for the filters style	
## Credits

## Author(s):blue_book:

Work is owned and maintained by 
	**`Imanol Asolo`**.

<3848@holbertonschool.com>

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Imanolasolo)
[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)](https://twitter.com/jjusturi)
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)](https://www.linkedin.com/in/imanol-asolo-5ba9b42a/)



## Acknowledgments :mega: 

### **`Holberton School`** (*providing guidance*)
	
This program was written as part of the curriculum for Holberton School.
Holberton School is a campus-based full-stack software engineering program
that prepares students for careers in the tech industry using project-based
peer learning. For more information,  please visit [this link](https://www.holbertonschool.com/).
![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)

---
title: Blog
---

<ul>
    {% for post in site.posts %}
        <li>
            <a href="{{ post.url }}">{{ post.title }}</a><br>
            {% assign d = post.date | date: "%-d" %}
            {%- case d %}
            {% when "1" or "21" or "31" %}{{ d }}st
                {% when "2" or "22" %}{{ d }}nd
                {% when "3" or "23" %}{{ d }}rd
                {% else %}{{ d }}th
            {%- endcase %} {{ post.date | date: "%B %Y" }}<br>
            {{ post.excerpt }}
        </li>
    {% endfor %}
</ul>

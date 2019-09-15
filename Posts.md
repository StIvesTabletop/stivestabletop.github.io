---
title: Blog
---

<ul class="postlist">
    {% for post in site.posts %}
        <li>
            <p><a href="{{ post.url }}">{{ post.title }}</a><br>
            <span class="postexcerpt">
            {% assign d = post.date | date: "%-d" %}
            {%- case d %}
            {% when "1" or "21" or "31" %}{{ d }}st
                {% when "2" or "22" %}{{ d }}nd
                {% when "3" or "23" %}{{ d }}rd
                {% else %}{{ d }}th
            {%- endcase %} {{ post.date | date: "%B %Y" }}</span></p>

            <span class="postexcerpt">{{ post.excerpt }}</span>
        </li>
    {% endfor %}
</ul>

# README

## XML formats for each individual component:
```xml
<xmldoc>
	<component value="rotor">
		<value="int 0-360"/>
	</component>
</xmldoc>

<xmldoc>
	<component value="temp">
		<value="int"/>
	</component>
</xmldoc>

<xmldoc>
	<component value="fanRPM">
		<value="int 0-100"/>
	</component>
</xmldoc>
```

## General idea:
```
script rotate---\                                                      /---fan change direction
                 \                                                    /
script temp-------|--Mainscript-->LoadToQueue-->Logic-->LoadOnQueue--|----------------fan start
                 /                                                    \
script fanRPM---/                                                      \---------fan rpm change
```

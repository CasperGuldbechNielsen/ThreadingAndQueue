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


script potentiometer (rotering)---------\					 	       /-------Blæser ændrer retning
					 \						      /
script temperatur (blæser)----------------|--Mainscript-->LoadToQueue-->Logic-->LoadOnQueue--|---------Blæser startes
					 /						      \
script potentiometer (blæser rpm)-------/					   	       \-------Blæser hastighed reguleres


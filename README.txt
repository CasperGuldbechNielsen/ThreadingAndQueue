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


script potentiometer (rotering)---------\					 	       /-------Bl�ser �ndrer retning
					 \						      /
script temperatur (bl�ser)----------------|--Mainscript-->LoadToQueue-->Logic-->LoadOnQueue--|---------Bl�ser startes
					 /						      \
script potentiometer (bl�ser rpm)-------/					   	       \-------Bl�ser hastighed reguleres


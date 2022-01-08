import React from 'react';
import {Link} from 'react-router-dom';
import {Button, Container} from 'react-bootstrap';
import logo from '../meeting-point.png';


export default function Landing() {
    return (
        <Container id="landing">
            <h1>MEET ME IN THE MIDDLE</h1>

            <img src={logo} alt='logo'/>
            
            <div id="desc">
            {"Having trouble deciding where to meet up with your friends because you can't decide on a central location? Fret not coz we are here to help. Just enter the nearest mrt stations of all your friends who are planning to meet up and leave the work to us. We guarantee to find you the best place to meet while ensuring that all of you travel nearly the same amount so no one has to go any further than the other. All you have to do is have fun with your friends!!"}
            </div>

            <Link to="/main">
            <Button variant='dark'>Get Started</Button>
            </Link>
            
        </Container>
    )
}

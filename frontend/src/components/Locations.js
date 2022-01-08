import React from 'react';
import {Col, Row, Container} from 'react-bootstrap';
import LocationCard from './LocationCard';

export default function Locations(props) {
    console.log(props.locList)
    return (
        <Container className='locations'>
            <h1>Here are our top 3 recommendations, as well as some interesting things to do there :)</h1>
        <Row style={{ justifyContent: "center", paddingBottom: "10px"}}>
                {props.locList.map((project, index) => {
                    return (
                        <Col md={4} key={index} className="project-card" style={{fontSize:"16px"}}>
                            <LocationCard name={project.name} thing={project.things}/>
                        </Col>  
                    );
                })}            
        </Row></Container>
    )
}

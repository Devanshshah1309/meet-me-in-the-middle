import React from 'react';
import {Col, Row, Container} from 'react-bootstrap';
import LocationCard from './LocationCard';

export default function Locations(props) {
    console.log(props.locList)
    return (
        <Container className='locations'>
        <Row style={{ justifyContent: "center", paddingBottom: "10px"}}>
                {props.locList.map((project, index) => {
                    return (
                        <Col md={4} key={index} className="project-card" style={{fontSize:"16px"}}>
                            <LocationCard name={project}/>
                        </Col>  
                    );
                })}            
        </Row></Container>
    )
}
